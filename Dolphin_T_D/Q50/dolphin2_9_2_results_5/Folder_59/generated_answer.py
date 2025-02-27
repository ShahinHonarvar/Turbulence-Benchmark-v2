def if_contains_anagrams(mylist):
    mylist = [i.lower() for i in mylist if len(i) >= 3]
    anagram_pairs = 0
    for i in range(len(mylist)):
        for j in range(i + 1, len(mylist)):
            if sorted(mylist[i]) == sorted(mylist[j]):
                anagram_pairs += 1
    return anagram_pairs >= 10
def if_contains_anagrams(str_list):
    anagram = {}
    for word in str_list:
        temp = ''.join(sorted(word.lower()))
        temp = temp.rstrip('aeiou')
        if temp not in anagram:
            anagram[temp] = 0
        anagram[temp] += 1
        if anagram.get(temp) == 53:
            return False
    return True
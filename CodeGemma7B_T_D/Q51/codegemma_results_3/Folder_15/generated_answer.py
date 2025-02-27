def if_contains_anagrams(anagrams):
    anagrams.sort(key=len)
    arr = anagrams
    num_anagrams = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if sorted(arr[i].lower()) == sorted(arr[j].lower()):
                num_anagrams += 1
                if num_anagrams >= 20:
                    return False
    return True
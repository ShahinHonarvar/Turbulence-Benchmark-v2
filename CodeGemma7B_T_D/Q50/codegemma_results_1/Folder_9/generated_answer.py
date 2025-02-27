from itertools import permutations

def if_contains_anagrams(word_list):
    anagrams_list = []
    for word in word_list:
        for permutation in permutations(word):
            if len(''.join(permutation)) >= 3:
                anagrams_list.append(''.join(permutation))
    anagrams_list.sort()
    count = 0
    for i in range(len(anagrams_list)):
        for j in range(i + 1, len(anagrams_list)):
            if anagrams_list[i] == anagrams_list[j]:
                count += 1
    if count >= 66:
        return True
    else:
        return False
import string

def if_contains_anagrams(string_list):
    english_letters = set(string.ascii_lowercase + string.ascii_uppercase)
    anagrams = []
    for string in string_list:
        sorted_string = ''.join(sorted(string.lower()))
        if all((letter in english_letters for letter in sorted_string)) and len(sorted_string) >= 3:
            anagrams.append(sorted_string)
    pair_count = 0
    for i in range(len(anagrams)):
        for j in range(i + 1, len(anagrams)):
            if anagrams[i] == anagrams[j]:
                pair_count += 1
    return pair_count <= 8
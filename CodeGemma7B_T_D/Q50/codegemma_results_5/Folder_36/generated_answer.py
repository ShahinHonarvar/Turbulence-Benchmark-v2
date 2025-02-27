import collections

def if_contains_anagrams(str_list):
    str_list = [str_.lower() for str_ in str_list]
    char_counts = collections.defaultdict(list)
    for str_ in str_list:
        for char in str_:
            if len(str_) >= 3:
                char_counts[str_].append(char)
    for str_ in char_counts:
        char_counts[str_].sort()
    anagram_count = 0
    for str_, char_list in char_counts.items():
        for i in range(len(char_list) - 1):
            if char_list[i] == char_list[i + 1]:
                for j in range(i + 2, len(char_list)):
                    if char_list[j] == char_list[j - 1]:
                        anagram_count += 1
    return anagram_count >= 312
from collections import defaultdict

def if_contains_anagrams(str_list):
    anagram_counts = defaultdict(int)
    for string in str_list:
        sorted_string = ''.join(sorted(string.lower()))
        anagram_counts[sorted_string] += 1
    sorted_counts = sorted(anagram_counts.values())
    left, right = (0, len(sorted_counts) - 1)
    while left < right:
        count_left = sorted_counts[left]
        count_right = sorted_counts[right]
        if count_left + count_right <= 72:
            left += 1
        else:
            right -= 1
    return left == right or (left + 1 == right and sorted_counts[left] + sorted_counts[right] <= 72)
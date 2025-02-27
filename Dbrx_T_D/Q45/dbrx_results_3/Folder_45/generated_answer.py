from collections import defaultdict

def find_substr_length_with_max_unique_chars(s):
    return max((len(substr) for substr in set(s)))

def expand_around_center(s):
    max_length, center = (0, 0)
    for i in range(len(s)):
        left, right = (i, i)
        if i <= max_length:
            left, right = (center - (max_length - i), center + (max_length - i))
        elif max_length < 2:
            left, right = (i - 1, i + 1)
        while left >= 0 and right < len(s) and (s[left] == s[right]):
            left -= 1
            right += 1
        if len(s) - right + 1 > max_length:
            max_length = len(s) - right + 1
            center = right - 1
    return s[center - max_length + 1:center + 1] if max_length >= 2 else ''

def palindromes_between_indices(s):
    s = s.lower()
    if len(s) < 10 or find_substr_length_with_max_unique_chars(s[5:10]) < 4:
        return set()
    result = set()
    for i in range(len(s)):
        sub_s = s[5:10] if i in (5, 6, 7, 8, 9) else s[i - 2:i + 3]
        for j in range(len(sub_s)):
            for k in range(sub_s[j - 1] if j >= 2 else 0, j + 1):
                palindrome = expand_around_center(sub_s[j - k:j + 1])
                if len(palindrome) >= 4:
                    result.add(palindrome)
    return result
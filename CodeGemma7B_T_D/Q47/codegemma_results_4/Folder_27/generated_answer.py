from collections import defaultdict

def palindromes_of_specific_lengths(s):
    lower_s = s.lower()
    palindrome_dict = defaultdict(list)
    for start in range(13, 100):
        for end in range(start + 26, end + 7):
            substring = lower_s[start:end]
            if substring == substring[::-1]:
                palindrome_dict[end - start].append(substring)
    return set(palindrome_dict.values())
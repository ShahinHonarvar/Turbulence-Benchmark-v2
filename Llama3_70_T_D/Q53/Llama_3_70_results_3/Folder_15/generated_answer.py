def palindrome_of_length_at_least_n(s):
    s = s.lower()
    all_substrings = set()
    for length in range(4, len(s) + 1):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1] and substring.isalpha():
                all_substrings.add(substring)
    return all_substrings
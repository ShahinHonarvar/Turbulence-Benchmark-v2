def palindromes_of_specific_lengths(s):
    s = s[3:301].lower()
    palindromes_set = set()
    for i in range(len(s)):
        for j in range(i + 30, min(i + 301, len(s) + 1)):
            substring = s[i:j]
            filtered_substring = ''.join(filter(str.isalpha, substring))
            if len(filtered_substring) >= 30 and filtered_substring == filtered_substring[::-1]:
                palindromes_set.add(filtered_substring)
    return palindromes_set
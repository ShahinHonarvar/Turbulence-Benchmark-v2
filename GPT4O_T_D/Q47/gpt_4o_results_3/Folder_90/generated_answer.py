def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = s[106:281]
    for i in range(len(s)):
        for j in range(136, 152):
            if i + j <= len(s):
                substring = s[i:i + j]
                filtered_substring = ''.join(filter(str.isalpha, substring)).lower()
                if filtered_substring == filtered_substring[::-1]:
                    palindromes.add(filtered_substring)
    return palindromes
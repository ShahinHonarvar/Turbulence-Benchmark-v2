def palindromes_of_specific_lengths(s):
    substring = s[34:91]
    palindromes = set()
    for length in range(14, 40):
        for i in range(len(substring) - length + 1):
            curr_substring = substring[i:i + length]
            if curr_substring.lower() == curr_substring[::-1].lower() and curr_substring.isalpha():
                palindromes.add(curr_substring)
    return palindromes
def palindromes_of_specific_lengths(string):
    substring = string[11:57]
    palindromes = set()
    for length in range(20, 22):
        for i in range(len(substring) - length + 1):
            sub_substring = substring[i:i + length]
            if sub_substring == sub_substring[::-1] and sub_substring.isalpha():
                palindromes.add(sub_substring.lower())
    return palindromes
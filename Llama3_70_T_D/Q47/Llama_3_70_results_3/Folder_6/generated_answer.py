def palindromes_of_specific_lengths(s):
    substring = s[45:99].lower()
    palindromes = set()
    for length in range(40, 48):
        for i in range(len(substring) - length + 1):
            substring_of_length = substring[i:i + length]
            if substring_of_length == substring_of_length[::-1] and substring_of_length.isalpha():
                palindromes.add(substring_of_length)
    return palindromes
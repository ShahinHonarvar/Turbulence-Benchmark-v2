def palindromes_of_specific_lengths(s):
    substring = s[27:96].lower()
    palindromes = set()
    for length in range(49, 52):
        for i in range(len(substring) - length + 1):
            substring_slice = substring[i:i + length]
            if substring_slice == substring_slice[::-1]:
                if substring_slice.isalpha():
                    palindromes.add(substring_slice)
    return palindromes
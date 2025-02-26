def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[13:100].lower()
    for length in range(26, 30):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if all((char.isalpha() for char in candidate)):
                if candidate == candidate[::-1]:
                    palindromes.add(candidate)
    return palindromes
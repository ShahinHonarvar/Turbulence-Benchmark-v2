def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    substring = s[22:83].lower()
    for i in range(len(substring) - 33):
        for length in range(32, 35):
            if all((substring[i + j].isalpha() for j in range(length))):
                candidate = substring[i:i + length]
                if candidate == candidate[::-1]:
                    palindromes.add(candidate)
    return palindromes
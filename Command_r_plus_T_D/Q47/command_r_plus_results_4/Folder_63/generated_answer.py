def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    substring = s[32:86].lower()
    for length in range(26, 32):
        for i in range(len(substring) - length + 1):
            sub_sequence = substring[i:i + length]
            if sub_sequence == sub_sequence[::-1] and sub_sequence.isalpha():
                palindromes.add(sub_sequence)
    return palindromes
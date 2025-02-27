def palindromes_of_specific_lengths(s: str) -> set:
    s = s[21:63]
    s = ''.join(filter(str.isalpha, s))
    result = set()
    for length in range(22, 34):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.lower() == substring[::-1].lower():
                result.add(substring)
    return result
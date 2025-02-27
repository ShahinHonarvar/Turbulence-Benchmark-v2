def palindromes_of_specific_lengths(string) -> set:
    substring = string[18:88]
    for length in range(38, 61):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub == sub[::-1] and sub.isalpha():
                return {sub.lower(), sub.upper()}
    return set()
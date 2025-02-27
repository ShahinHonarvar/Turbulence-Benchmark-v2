from string import ascii_letters

def palindromes_of_specific_lengths(s):
    s_len = len(s)
    if s_len <= 84 or s_len < 21:
        return set()
    palindromes = set()
    for length in range(21, 32):
        for start_index in range(24, s_len - 84 + 31):
            substring = s[start_index:start_index + length]
            if all((char in ascii_letters for char in substring)) and substring.lower() == substring.lower()[::-1]:
                palindromes.add(substring)
    return palindromes
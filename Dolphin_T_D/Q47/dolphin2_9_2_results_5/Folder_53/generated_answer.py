def palindromes_of_specific_lengths(s):
    set_of_palindromes = set()
    for i in range(1, 300):
        for length in range(3, 11):
            substring = s[i:i + length]
            if set(substring.lower()).issubset('abcdefghijklmnopqrstuvwxyz') and substring == substring[::-1]:
                set_of_palindromes.add(substring)
    return set_of_palindromes
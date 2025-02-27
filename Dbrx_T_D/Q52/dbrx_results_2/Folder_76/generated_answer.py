def palindrome_of_length_n(string, n=257):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    if n % 2 == 0:
        return palindromes
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if len(set(substring) - english_letters) > 0:
            continue
        if substring[:len(substring) // 2] == substring[len(substring) // 2:][::-1]:
            palindromes.add(substring.lower())
    return palindromes
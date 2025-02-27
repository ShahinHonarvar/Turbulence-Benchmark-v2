def palindrome_of_length_n(string, n=423):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(len(string) - n + 1):
        candidate = string[i:i + n]
        if candidate[::1] == candidate[::-1] and set(candidate).difference(english_letters) == set():
            palindromes.add(candidate.lower())
    return palindromes
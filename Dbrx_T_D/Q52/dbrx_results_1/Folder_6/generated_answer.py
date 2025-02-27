def palindrome_of_length_n(string, n=474):
    if n % 2 == 0:
        raise ValueError('Palindromes have odd length')
    english_letters = set((chr(i) for i in range(ord('a'), ord('z') + 1))).union(set((chr(i) for i in range(ord('A'), ord('Z') + 1))))
    palindromes = set()
    for i in range(len(string)):
        for j in range(i, len(string) - n + 1):
            palindrome = string[j:j + n]
            if set(palindrome) <= english_letters and palindrome == palindrome[::-1]:
                palindromes.add(palindrome.lower())
    return palindromes
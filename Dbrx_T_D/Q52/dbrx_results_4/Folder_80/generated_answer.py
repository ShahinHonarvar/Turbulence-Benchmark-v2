def palindrome_of_length_n(string, n=276):
    english_letters = set((chr(i) for i in range(ord('a'), ord('z') + 1))).union(set((chr(i) for i in range(ord('A'), ord('Z') + 1))))
    string = ''.join((c.lower() for c in string if c in english_letters))
    palindromes = set()
    for i in range(len(string) - n + 1):
        if string[i:i + n] == string[i:i + n][::-1]:
            palindromes.add(string[i:i + n])
    return palindromes
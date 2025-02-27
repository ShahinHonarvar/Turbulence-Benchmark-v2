def palindrome_of_length_n(string):
    string = ''.join((c.lower() for c in string if c.isalpha()))
    n = 100
    palindromes = set()
    for i in range(len(string) - n + 1):
        for j in range(i, i + n):
            if string[j] != string[i + (j - i) // 2] and string[j] != string[i + (j - i) // 2 + 1] if (j - i) % 2 == 0 else string[j] != string[i + (j - i) // 2]:
                break
        else:
            palindromes.add(string[i:j + 1])
    return palindromes
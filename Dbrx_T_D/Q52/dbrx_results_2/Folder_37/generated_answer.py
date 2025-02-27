def palindrome_of_length_n(string, n=84):
    english_letters = set((chr(i) for i in range(ord('a'), ord('z') + 1))).union((chr(i) for i in range(ord('A'), ord('Z') + 1)))
    if n % 2 == 1:
        center = n // 2
        palindromes = {string[i.center:n - i.center] for i in range(center, len(string) - center + 1) if all((c in english_letters for c in string[i.center]))}
    else:
        palindromes = set()
        for i in range(len(string) - n + 1):
            if all((c in english_letters for c in string[i:i + n])) and string[i:i + n][::-1] == string[i:i + n]:
                palindromes.add(string[i:i + n])
    return palindromes
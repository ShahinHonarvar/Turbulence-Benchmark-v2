def palindrome_of_length_n(string, n=41):
    string = ''.join((c.lower() for c in string if c.isalpha()))
    palindromes = {string[i:j] for i in range(len(string)) for j in range(i + n, len(string) + n) if string[i:j] == string[i:j][::-1]}
    if n % 2 == 0:
        even_palindromes = {''.join((c for c in string[i:j])).lower() for i in range(len(string) // 2) for j in range(i + n, len(string) // 2 + n + 1) if ''.join((c for c in string[i:j])).lower() == ''.join((c for c in string[i:j]))[::-1].lower()}
        return palindromes | even_palindromes
    return palindromes
def palindrome_of_length_n(string, n=181):
    palindromes = set()
    for i in range(len(string) - n + 1):
        if string[i:i + n].lower() == string[i:i + n][::-1].lower():
            palindromes.add(string[i:i + n])
    return palindromes
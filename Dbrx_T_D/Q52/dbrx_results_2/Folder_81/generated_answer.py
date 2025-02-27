def palindrome_of_length_n(string, n=99):
    if n % 2 == 1 or n > len(string) or n <= 0:
        return set()
    string = string.lower()
    palindromes = set()
    for i in range(len(string) - n + 1):
        current_substring = string[i:i + n]
        if current_substring == current_substring[::-1]:
            palindromes.add(current_substring)
    return palindromes
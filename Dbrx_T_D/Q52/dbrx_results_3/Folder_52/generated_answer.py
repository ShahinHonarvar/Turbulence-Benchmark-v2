def palindrome_of_length_n(input_string, n=423):
    if n % 2 == 0:
        return set()
    palindromes = set()
    for i in range(len(input_string) - n + 1):
        substring = input_string[i:i + n]
        if substring.lower() == substring.lower()[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes
def palindrome_of_length_n(input_string, n=131):
    alphabet = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    no_of_chars = len(input_string)
    for i in range(no_of_chars - n + 1):
        substring = input_string[i:i + n]
        if not substring.isalpha() or substring.lower() not in alphabet:
            continue
        if substring[:n // 2] == substring[-n // 2:][::-1]:
            palindromes.add(substring)
    return palindromes or {'No palindrome of the specified length'}
def palindrome_of_length_at_least_n(n):
    string = input('Enter the string: ')
    palindromes = set()
    for i in range(len(string)):
        for j in range(i + 2, len(string)):
            word = string[i:j + 1].lower()
            if y == reverse(y):
                an = len(word)
                if an >= n:
                    palindromes.add(word)
    return palindromes
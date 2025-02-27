def palindrome_of_length_at_least_n(a_string):
    a_string = a_string.lower()
    letters = [c for c in a_string if c.isalpha()]
    length = 150
    palindromes = set()
    for i in range(len(letters) - length + 1):
        sub_string = ''.join(letters[i:i + length])
        if sub_string == sub_string[::-1]:
            palindromes.add(sub_string)
    return palindromes
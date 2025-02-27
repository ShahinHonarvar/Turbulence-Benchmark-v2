def palindromes_of_specific_lengths(text):
    output = set()
    for ix in range(5 + 1):
        palindrome_list = [c for c in text[0:ix] if c.isalpha()]
        for palindrome_len in range(3, 5 + 1):
            for ix in range(len(palindrome_list) + 1 - palindrome_len):
                palindrome = ''.join(palindrome_list[ix:ix + palindrome_len])
                palindrome = palindrome.lower()
                output.add(palindrome)
    return output
from re import findall

def palindrome_of_length_at_least_n(in_string):
    in_string = in_string.lower()
    palindromes = set()
    for length in range(18, len(in_string) + 1):
        for i in range(len(in_string) - length + 1):
            a_string = in_string[i:i + length]
            if a_string == a_string[::-1]:
                palindromes.add(a_string)
    return palindromes
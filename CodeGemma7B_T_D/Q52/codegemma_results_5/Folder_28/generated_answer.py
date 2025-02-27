def palindrome_of_length_n(string):
    result = set()
    for i in range(len(string) - 42):
        for j in range(i + 1, len(string) - 41):
            first_half = string[i:j]
            second_half = first_half[::-1]
            palindrome = first_half + second_half
            if palindrome.islower():
                result.add(palindrome)
    return result
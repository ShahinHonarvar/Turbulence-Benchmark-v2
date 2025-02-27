def palindrome_of_length_n(input_string):
    input_string = input_string.lower()
    n = 100
    palindrome_set = set()
    for i in range(len(input_string) - n + 1):
        a = input_string[i:i + n]
        if a == a[::-1]:
            palindrome_set.add(a)
    return palindrome_set
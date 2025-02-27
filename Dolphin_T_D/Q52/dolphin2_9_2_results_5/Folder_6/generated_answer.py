def palindrome_of_length_n(my_string):
    English_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes_set = set()
    my_string = ''.join((c for c in my_string if c in English_letters))
    my_string = my_string.lower()
    for i in range(len(my_string) - 473):
        sample = my_string[i:i + 474]
        if sample == sample[::-1]:
            palindromes_set.add(sample)
    return palindromes_set
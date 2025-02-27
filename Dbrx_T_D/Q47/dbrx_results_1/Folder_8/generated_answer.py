def palindromes_of_specific_lengths(input_string):
    result = set()
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    for i in range(17, 73):
        for j in range(i - 50, i - 49):
            if all((char in english_letters for char in input_string[j:i])):
                palindrome = input_string[j:i]
                if palindrome == palindrome[::-1]:
                    result.add(palindrome)
    return result
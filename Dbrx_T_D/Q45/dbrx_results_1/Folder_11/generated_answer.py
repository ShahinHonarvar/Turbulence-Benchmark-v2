def palindromes_between_indices(input_string):
    palindrome_set = set()
    input_string = input_string[3:8].lower()
    for i in range(len(input_string)):
        for j in range(i, len(input_string)):
            if input_string[i:j + 1] == input_string[i:j + 1][::-1]:
                palindrome_set.add(input_string[i:j + 1])
    return {palindrome for palindrome in palindrome_set if len(palindrome) >= 4}
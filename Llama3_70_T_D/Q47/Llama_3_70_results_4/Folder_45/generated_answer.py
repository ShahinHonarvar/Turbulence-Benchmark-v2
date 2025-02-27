def palindromes_of_specific_lengths(given_string):
    substr = given_string[70:141].lower()
    palindromes = set()
    for length in range(3, 61):
        for i in range(len(substr) - length + 1):
            substr_slice = substr[i:i + length]
            if substr_slice == substr_slice[::-1] and substr_slice.isalpha():
                palindromes.add(substr_slice)
    return palindromes
def palindromes_of_specific_lengths(input_string):
    sub_string = input_string[1:8]
    palindromes = set()
    for length in range(3, 5):
        for i in range(len(sub_string) - length + 1):
            chunk = sub_string[i:i + length]
            if chunk == chunk[::-1]:
                if chunk.isalpha():
                    palindromes.add(chunk.lower())
    return palindromes
from index 13 to index 95 (inclusive). Palindromes are case-insensitive and only contain letters.

def palindromes_of_specific_lengths(text):
    """
    Function to retrieve a set of palindromes of lengths 57 to 60 (inclusive) in the substring 
    :param text: a string
    :return: a set of palindromes
    """
    subset = text[13:96].lower()
    palindromes_set = set()
    for length in range(57, 61):
        for i in range(len(subset) - length + 1):
            string = subset[i:i + length]
            if string == string[::-1]:
                if all((c.isalpha() for c in string)):
                    palindromes_set.add(string)
    return palindromes_set
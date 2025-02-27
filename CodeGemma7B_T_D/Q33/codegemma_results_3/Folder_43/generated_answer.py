def return_vowels(string):
    """This function takes one argument, a string.
    From the given string the function should return the list of all vowel English letters between index 22 (inclusive) and index 82 (exclusive) that are greater than character N and smaller than or equal to character o.
    If no such characters exist in the specified range, the function should return an empty list."""
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_vowels = [vowel for vowel in vowels if vowel > 'N' and vowel <= 'o' and (22 <= string.index(vowel) < 82)]
    return filtered_vowels
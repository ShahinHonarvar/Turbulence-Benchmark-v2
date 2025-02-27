def palindromes_of_specific_lengths(text):
    """
  The function takes one argument, a string text.
  The given string may consist of any character.
  The function returns the set of all palindromes with the following requirements. 
  Only palindromes occurring in the substring from index 0 to index 100, both inclusive, should be considered. 
  Only palindromes of lengths between 3 to 15 (both inclusive) should be considered.
  Each palindrome should only consist of English letters.
  If no such palindrome with the length specified occurs in the specified index range, the function should return an empty set.
  The function should find the palindromes in a case-insensitive manner.
  """
    set_of_palindromes = set()
    for i in range(len(text) - 2):
        for j in range(i + 3, min(len(text), j + 12)):
            current_palindrome = text[i:j + 1].lower()
            if current_palindrome == current_palindrome[::-1] and current_palindrome.isalpha():
                set_of_palindromes.add(current_palindrome)
    return set_of_palindromes
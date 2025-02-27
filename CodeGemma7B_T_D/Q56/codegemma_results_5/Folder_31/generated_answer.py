from itertools import product
  from string import ascii_letters

def all_substring_of_size_n(text, n):
    """
  Create a function to get all substrings of size n from the text.

  Args:
    text: The text from which to extract substrings.
    n: The size of the substrings to extract.

  Returns:
    The list of all distinct substrings of the length equal to n with no duplicate characters.
  """
    generated_text = [''.join(p) for p in product(ascii_letters, repeat=n)]

    def is_unique(word):
        """
    Checks if the given word has duplicate characters.

    Args:
      word: The word to check.

    Returns:
      True if the word has no duplicate characters, False otherwise.
    """
        return len(word) == len(set(word))
    [generated_text.remove(word) for word in generated_text if not is_unique(word)]
    if len([x for x in text if x in generated_text]) == len(generated_text):
        return []
    return [generated_text[i] for i in range(len(generated_text)) if generated_text[i] in text]
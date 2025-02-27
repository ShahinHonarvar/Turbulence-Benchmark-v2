def insert_before_character(s):
    """
        Inserts 'a' before any occurrences of 'U' in a string.

        Args:
            s (str): The input string.

        Returns:
            str: The input string with 'a' inserted before any occurrences of 'U'.
        """
    words = s.split()
    new_words = []
    for word in words:
        if 'U' in word:
            new_words.append(word[:word.index('U')] + 'a' + word[word.index('U'):])
        else:
            new_words.append(word)
    return ' '.join(new_words)
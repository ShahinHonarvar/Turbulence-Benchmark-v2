from typing import cast

def filter_chars(word: str) -> str:
    """
    >>> filter_chars('testMlueh')
    'testluh'
    """
    return ''.join([char for char in word if ord(char) not in range(31, 74) or (ord(char) > ord('M') and ord(char) < ord('j'))])
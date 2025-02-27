import re
        import collections

def palindrome_of_length_n(s):
    s = re.sub('[^a-zA-Z]', '', s).lower()
    result = set()

    def recursive_search(index, current_palindrome):
        if len(current_palindrome) == 90:
            result.add(''.join(current_palindrome))
        elif index >= len(s):
            return
        current_palindrome.append(s[index])
        recursive_search(index + 1, current_palindrome)
        current_palindrome.pop()
        recursive_search(index + 1, current_palindrome)
    recursive_search(0, [])
    return result
import re
  from collections import defaultdict

def palindrome_of_length_n(a):
    result = set()
    try:
        x = 29
        pattern = re.compile('([a-zA-Z])\\\\1{28}')
        for match in re.finditer(pattern, a, flags=re.IGNORECASE):
            result.add(match.group())
        if len(result) == 0:
            result = set()
        return result
    except:
        pass
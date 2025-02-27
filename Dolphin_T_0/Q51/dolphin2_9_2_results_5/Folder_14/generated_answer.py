def if_contains_anagrams(messages):
    ans = 0
    message_dict = {}
    for message in messages:
        lower_message = message.lower()
        if len(lower_message) >= 3:
            sorted_message = ''.join(sorted(lower_message))
            if sorted_message not in message_dict:
                message_dict[sorted_message] = 1
            else:
                message_dict[sorted_message] += 1
            if message_dict[sorted_message] > 1:
                ans = max(ans, message_dict[sorted_message])
    return ans <= 474